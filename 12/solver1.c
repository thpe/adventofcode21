#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct vlist {
  char name[6];
  int val;
  int visited;
  int maxvisit;
  struct vlist* prev;
  struct vlist* neig;
  struct vlist* next;
} vlist_t;

vlist_t* prepend(vlist_t* next, const char* name)
{
  //printf("add %s.\n", name);
  vlist_t* ptr = (vlist_t*) malloc (sizeof(vlist_t));
  memset(ptr, 0, sizeof(vlist_t));
  strcpy(ptr->name, name);
  ptr->next = next;
  if(next != NULL) {
    next->prev = ptr;
  }
  return ptr;
}
vlist_t* add(vlist_t* prev, const char* name)
{
  vlist_t* ptr = (vlist_t*) malloc (sizeof(vlist_t));
  memset(ptr, 0, sizeof(vlist_t));
  strcpy(ptr->name, name);
  if (name[0] < 'a') {
    ptr->maxvisit = 2;
  } else {
    ptr->maxvisit = 1;
  }
  ptr->prev = prev;
  if(prev != NULL) {
    prev->next = ptr;
  }
  printf("add %s %d.\n", name, ptr->maxvisit);
  return ptr;
}

vlist_t* search(vlist_t* ptr, const char* name)
{
  while (ptr != NULL) {
    if (0 == strcmp(name, ptr->name)) {
      //printf("found %s.\n", name);
      break;
    }
    ptr = ptr->next;
  }
  return ptr;
}

void printGraph(vlist_t* start)
{
  vlist_t* gptr = start;
  while(gptr != NULL) {
    printf("%s %d %d:", gptr->name, gptr->visited, gptr->maxvisit);
    vlist_t* nptr = gptr->neig;
    while(nptr != NULL) {
      printf("%s,", nptr->name);
      nptr = nptr->next;
    }
    printf(".\n");

    gptr = gptr->next;
  }
}
int isStart(char *str) {
  return 0 == strncmp(str, "start", 5);
}
int isEnd(char *str) {
  return 0 == strncmp(str, "end", 3);
}

int dfs(vlist_t* start, int count)
{
  if (start->visited < 1 || start->maxvisit == 2) {

    start->visited++;

    vlist_t* ptr = start->neig;
    while (ptr != NULL) {
      if (isEnd(ptr->name)) {
        count++;
      } else {
        count = dfs(ptr->neig, count);
      }
      ptr = ptr->next;
    }

    start->visited--;

  }
  return count;
}

int main(int argc, char** argv)
{

  FILE* f;
  ssize_t chars;
  size_t len;
  char* line;
  int i;
  int cnt = 0;
  vlist_t* start = add((vlist_t*)NULL, "start");
  vlist_t* end = add(start, "end");
  vlist_t* last = end;
  char from[6];
  char to[6];
  vlist_t* ptr = NULL;

  if (argc != 2) {
    printf("there should be exactly on arg, but there where %d", argc);
  }

  f = fopen(argv[1], "r");

  if (f == NULL) {
    perror("error opening file");
    exit(EXIT_FAILURE);
  }



  while (!feof(f)) {
    int idx = 0;
    char c;
    while(1) {
      c = fgetc(f);
      if (c == '-' || c == EOF) {
        from[idx++] = '\00';
        break;
      }
      from[idx++] = c;
    }
    idx = 0;
    while(1) {
      c = fgetc(f);
      if (c == '\n' || c == EOF) {
        to[idx++] = '\00';
        break;
      }
      to[idx++] = c;
    }
    if (to[0] == 0 || from[0] == 0) {
      break;
    }
    printf("%s -> %s.\n", from, to);
    vlist_t* ptr_to = search(start, to);
    if (ptr_to == NULL) {
      cnt++;
      last = add (last, to);
      ptr_to = last;
    }
    vlist_t* ptr_from = search(start, from);
    if (ptr_from == NULL) {
      cnt++;
      last = add (last, from);
      ptr_from = last;
    }


    ptr_to->neig = prepend (ptr_to->neig, from);
    ptr_to->neig->neig = ptr_from;
    cnt++;

    ptr_from->neig = prepend (ptr_from->neig, to);
    ptr_from->neig->neig = ptr_to;
    cnt++;



  }
  printf("allocated %d elements.\n", cnt+2);
  fclose (f);


  printGraph(start);
  int count = dfs(start, 0);
  printf("res %d.\n", count);

  cnt = 0;
  vlist_t* next = NULL;
  while (start != NULL) {
    while (start->neig != NULL) {
      next = start->neig->next;
      free (start->neig);
      start->neig = next;
      cnt++;
    }
    next = start->next;
    free(start);
    start = next;
    cnt++;
  }
  printf("deallocated %d elements.\n", cnt);
  exit(EXIT_SUCCESS);
}

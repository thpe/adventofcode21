#include <stdio.h>
#include <stdlib.h>


typedef struct list {
  int val;
  struct list* prev;
  struct list* next;
} list_t;

int main(int argc, char** argv)
{

  FILE* f;
  ssize_t chars;
  size_t len;
  char* line;
  int i;
  int cnt = 0;
  list_t* l = NULL;
  list_t* last = NULL;
  list_t* ptr = NULL;

  if (argc != 2) {
    printf("there should be exactly on arg, but there where %d", argc);
  }

  f = fopen(argv[1], "r");

  if (f == NULL) {
    perror("error opening file");
    exit(EXIT_FAILURE);
  }



  // is it really necessary to have a list here, instead of computing on the fly? No :-)
  while (!feof(f)) {
    fscanf(f, "%d", &i);
    if (l == NULL) {
      l = (list_t*) malloc (sizeof(list_t));
      last = l;
      l->prev = NULL;
      l->next = NULL;
    } else {
      last->next = (list_t*) malloc(sizeof(list_t));
      last->next->prev = last;
      last = last->next;
    }
    cnt++;
    last->val = i;
    last->next = NULL;
  }

  printf("allocated %d elements.\n", cnt);
  fclose (f);

  ptr = l->next;
  cnt = 0;
  while (ptr != NULL) {
    if (ptr->prev->val < ptr->val) {
      cnt++;
    }
    if (ptr->next != NULL) {
      ptr = ptr->next;
    } else {
      break;
    }
  }
  printf("res %d.\n", cnt);

  while (l != NULL) {
    list_t* next = l->next;
    free(l);
    l = next;
  }
  exit(EXIT_SUCCESS);
}

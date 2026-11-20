#include <ctype.h>

char *strupr(char *var){
    for(int i = 0; var[i] != '\0' ; i++){
        var[i] = toupper(var[i]);
    }
    return var;
}

char *strlwr(char *var){
    for(int i = 0; var[i] != '\0' ; i++){
        var[i] = tolower(var[i]);
    }
    return var;
}
#include<stdio.h>
#include<stdlib.h>
#include<conio.h> 
#include<direct.h>
#define H 15
#define W 40
char playfield[H][W]={
{"****************************************"},
{"* .....................................*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*......................................*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*..*..*..*..*..*..*..*..*..*..*..*..*..*"},
{"*......................................*"},
{"****************************************"}
}; //this is our playfield

int food_collect=0,game_end=0;
int py=1,px=1;//these variables represent pacman coordinate
int gy1=1,gx1=38,gy2=13,gx2=1;//these variables represent ghosts coordinate
void game_result()
{
//this function check you won the game or not
  getchar();
   system("cls");
  if(food_collect==500)
  {
    printf("\n\n\n\n\n\n\n\n\n");
    printf("\t\t\t        Congratulation!\n");
    printf("\t\t\t       You won the game!\n");
    printf("\t\t\t     Your total score is %d",food_collect);
  }
  else
  {
    printf("\n\n\n\n\n\n\n\n\n");
    printf("\t\t\t          Better luck!\n");
    printf("\t\t\t       You lose the game!\n");
    printf("\t\t\t     Your total score is %d\n",food_collect);
  }
}
void move_ghosts()
{
 if(gy1==1 && gx1 > 1)
 {
   gx1--; //this statement move 1st ghost coordinate to left side
 }
 else if(gx1 == 1 && gy1 < 7)
 {
   gy1++; //this statement move 1st ghost coordinate to down side
 }
 else if(gy1 == 7 && gx1 < 38)
 {
   gx1++; //this statement move 1st ghost coordinate to right side
 }
 else if(gx1 == 38 && gy1 > 1)
 {
   gy1--; //this statement move 1st ghost coordinate to up side
 }

 if(gy2 == 13 && gx2 < 38)
 {
   gx2++; //this statement move 2nd ghost coordinate to right side
 }
 else if(gx2 == 38 && gy2 > 7)
 {
   gy2--; //this statement move 2nd ghost coordinate to up side
 }
 else if(gy2 == 7 && gx2 > 1)
 {
   gx2--; //this statement move 2nd ghost coordinate to left side
 }
 else if(gx2 == 1 && gy2 < 13)
 {
   gy2++; //this statement move 2nd ghost coordinate to down side
 }
}
void user_input()
{
//this function use to take user input
 char c1;
 if(kbhit())
 {
   c1=getch();

   switch(c1)
   {
     case 72:py-=1;break; //cursor up
     case 80:py+=1;break; //cursor down
     case 75:px-=1;break; //cursor left
     case 77:px+=1;break; //cursor right
   }
 }
}
void setup()
{
int a,i,j;
for(i=0;i < H;i++)
{
  for(j=0;j < W;j++)
  {
    if(playfield[i][j]=='#')
    {
      playfield[i][j]=' ';
    }
    if(playfield[i][j]=='@')
    {
      playfield[i][j]='.';
    }
  }
}
if(playfield[py][px]=='.')
{
  food_collect++;
}
if(playfield[py][px]=='*')
{
  py=1;
  px=1;
}
playfield[py][px]='#';
playfield[gy1][gx1]='@';
playfield[gy2][gx2]='@';

if(playfield[py][px]=='@')
{
  game_end=1;
}
}
void draw_playfield()
{
int i,j;
printf("\033[0;31m");
printf("\n\n\n\n");
for(i=0;i < H;i++)
{
  printf("\t\t");
  for(j=0;j < W;j++)
  {
    printf("%c",playfield[i][j]);
  }
  printf("\n");
}
printf("Score is %d ",food_collect);
}

void main()
{
int i=100;
while(game_end!=1)
{
  getchar();
   system("cls");
  sound(i);  //to produce sound
  setup();
  user_input();
  move_ghosts();
  draw_playfield();
  delay(200);
  if(i < 1000)
  i=i+100;
  else
  i=100;
}
nosound(); //to close sound
game_result();
getch();
}
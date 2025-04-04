import java.util.ArrayList;

public class Snake {
    ArrayList<int[]> snake;
    int len;
    Direction dir;
    public Snake(int l,int w,int h){
        snake= new ArrayList<>();
        len=l;
        for (int i = 0; i < l; i++) {
            int[] k= {h/2+i,w/2};
            snake.add(k);
        }
    }
    public void move(Direction d,Board b){
        int[] dir;
        if(d==Direction.U){
            dir= new int[]{-1,0};
        }else if(d==Direction.D){
            dir= new int[]{1, 0};
        }else if(d==Direction.L){
            dir= new int[]{0,-1};
        }else{
            dir= new int[]{0, 1};
        }
        int y=snake.get(0)[0]+dir[0];
        int x=snake.get(0)[1]+dir[1];
        ArrayList<int[]> res = new ArrayList<>();
        if(b.board[y][x]==0||b.board[y][x]==9){//si on ne va pas OOB ou sur sois meme on avance
            res.add(new int[]{y,x});
            b.currDir=d;
            if(b.board[y][x]==9){//si on mange une pomme on ajoute 1 a la len
                len++;
                b.score.addApple();
                b.apple.placeNew(b.board);
            }
        }else {//sinon on declenche un gameover
            b.gameOver();
        }
        for (int i = 0; i < len-1; i++) {//on copie l'ancien snake dans le nouveau
            res.add(snake.get(i));
        }
        this.dir=d;
        snake=res;
    }
}

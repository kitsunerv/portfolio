public class AI {
//b.board[b.snake.snake.get(0)[0]+ai.d1[0]][b.snake.snake.get(0)[1]+ai.d1[1]]
    public static Direction move(Board b){
        int x=0,y=0;
        Direction res;
        if(b.snake.snake.get(0)[0]<b.apple.y){
            y=1;
        }else if(b.snake.snake.get(0)[0]>b.apple.y){
            y=-1;
        }
        if(b.snake.snake.get(0)[1]<b.apple.x){
            x=1;
        }else if(b.snake.snake.get(0)[1]>b.apple.x){
            x=-1;
        }
        res = calculate(x,y);
        AiManeuvres ai = new AiManeuvres(b,res);
        int i=0;
        int y1=b.snake.snake.get(0)[0]+ai.d1[0];
        int x1=b.snake.snake.get(0)[1]+ai.d1[1];
        int t =b.board[y1][x1];
        while ((isCulDeSac(b,new int[]{y1,x1})||(t!=0&&t!=9))&&i<10){
            ai.next();
            y1=b.snake.snake.get(0)[0]+ai.d1[0];
            x1=b.snake.snake.get(0)[1]+ai.d1[1];
            t =b.board[y1][x1];
            i++;
        }
        if(i>9){
            System.out.println("idk somthing failed in the loop");
            return b.currDir;
        }
        else{
            res= ai.d;
        }
        return res;
    }
    static int[] convert(Direction d) {
        if (d == Direction.U) {
            return new int[]{-1, 0};
        } else if (Direction.D == d) {
            return new int[]{1, 0};
        } else if (Direction.L == d) {
            return new int[]{0, -1};
        } else {
            return new int[]{0, 1};
        }
    }
    public static boolean isCulDeSac(Board b,int[] coord){
        int res=0;
        if ((b.board[coord[0]+1][coord[1]]!=0)&&(b.board[coord[0]+1][coord[1]]!=9)){
            res+=1;
        }
        if ((b.board[coord[0]-1][coord[1]]!=0)&&(b.board[coord[0]-1][coord[1]]!=9)){
            res+=1;
        }
        if ((b.board[coord[0]][coord[1]+1]!=0)&&(b.board[coord[0]][coord[1]+1]!=9)){
            res+=1;
        }
        if ((b.board[coord[0]][coord[1]-1]!=0)&&(b.board[coord[0]][coord[1]-1]!=9)){
            res+=1;
        }
        return (res==4);
    }
    static Direction calculate(int x,int y){
        //linear mode
        if(y==-1){
            return Direction.U;
        }else if(y==1){
            return Direction.D;
        }else if(x==-1){
            return Direction.L;
        }else{
            return Direction.R;
        }
    }
    static int abs(int i){
        if (i<0){
            return -1;
        }else if(i>0){
            return 1;
        }else {
            return 0;
        }
    }
}


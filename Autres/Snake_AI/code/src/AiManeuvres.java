public class AiManeuvres {
    StrategieMouvement strat;
    Direction d;
    int[] d1;
    Board b;
    public AiManeuvres(Board b,Direction d){
        this.b=b;
        this.d=d;
        this.d1=AI.convert(d);
        strat=decide(this.b,this.d);
    }
    public StrategieMouvement decide(Board b,Direction d){
        int x=0;
        int[] d5=AI.convert(b.currDir);
        if (b.board[b.snake.snake.get(0)[0]+d5[0]][b.snake.snake.get(0)[1]+d5[1]]==2){
            System.out.println("sigma");
            return new Sigma();
        }
        if (b.board[b.snake.snake.get(0)[0]+d5[0]][b.snake.snake.get(0)[1]+d5[1]]==5){
            System.out.println("sigmawall");
            return new SigmaWall();
        }
        if (b.snake.snake.get(0)[1]>b.apple.x){
            x=-1;
        }else if(b.snake.snake.get(0)[1]<b.apple.x){
            x=1;
        }
        int y=0;
        if (b.snake.snake.get(0)[0]>b.apple.y){
            y=-1;
        }else if(b.snake.snake.get(0)[0]<b.apple.y){
            y=1;
        }
        if((y==-1&&d==Direction.L)||
                (y==1&&d==Direction.R)||
                (x==-1&&d==Direction.D)||
                (x==1&&d==Direction.U)){
            System.out.println("clockwise");
            return new Clockwise();
        }else {
            System.out.println("anticlockwise");
            return new AntiClockwise();
        }
    }


    public void next(){
        this.d=strat.process(d, b.snake);
        d1=AI.convert(d);
    }
}

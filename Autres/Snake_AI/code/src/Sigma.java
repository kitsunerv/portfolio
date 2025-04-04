public class Sigma implements StrategieMouvement{
    @Override
    public Direction process(Direction d,Snake s) {
       int[] d1 =AI.convert(s.dir);
       int x= s.snake.get(0)[1]+d1[1];
       int y= s.snake.get(0)[0]+d1[0];
       int t=1;
        for (int i = 0; i < s.len; i++) {
            if(s.snake.get(0)[1]==x&&s.snake.get(0)[0]==y){
                t=i;
            }
        }
        t=t/2;
        int[] d2 = compare(s.snake.get(0),s.snake.get(t));
        try{
            int[] d3 = compare(s.snake.get(0),s.snake.get(t-2));
            int[] d4 = compare(s.snake.get(0),s.snake.get(t+2));
            d2[0]+=d3[0]+d4[0];
            d2[1]+=d3[1]+d4[1];
            d2[0]=AI.abs(d2[0]);
            d2[1]=AI.abs(d2[1]);
        }catch (Exception ignored){}
        if((s.dir==Direction.U&&d2[1]==1)||(s.dir==Direction.D&&d2[1]==1)){
            return Direction.L;
        }else if((s.dir==Direction.U&&d2[1]==-1)||(s.dir==Direction.D&&d2[1]==-1)){
            return Direction.R;
        }else if((s.dir==Direction.L&&d2[0]==1)||(s.dir==Direction.R&&d2[0]==1)){
            return Direction.U;
        }else {
            return Direction.D;
        }
    }

    public static int[] compare(int[] p1,int[] p2){
        int x=0,y=0;
        if(p1[0]>p2[0]){
            y=1;
        }else{
            y=-1;
        }
        if(p1[1]>p2[1]){
            x=1;
        }else{
            x=-1;
        }
        return new int[]{y,x};
    }
}

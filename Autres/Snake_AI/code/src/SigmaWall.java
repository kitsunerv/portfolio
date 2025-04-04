public class SigmaWall implements  StrategieMouvement{
    @Override
    public Direction process(Direction d, Snake s) {
        int x =0;
        int y =0;
        for (int i = s.len/4; i < s.len; i+=s.len/4) {
            x+=AI.abs(s.snake.get(i)[1]);
            y+=AI.abs(s.snake.get(i)[0]);
        }
        if((s.dir==Direction.U&&x==1)||(s.dir==Direction.D&&x==1)){
            return Direction.L;
        }
        else if((s.dir==Direction.U&&x==-1)||(s.dir==Direction.D&&x==-1)){
            return Direction.R;
        }
        else if((s.dir==Direction.L&&y==1)||(s.dir==Direction.R&&y==1)){
            return Direction.U;
        }
        else if((s.dir==Direction.L&&y==-1)||(s.dir==Direction.R&&y==-1)){
            return Direction.D;
        }else {
            return d;
        }
    }
}

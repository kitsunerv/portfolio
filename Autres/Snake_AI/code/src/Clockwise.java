public class Clockwise implements StrategieMouvement{
    @Override
    public Direction process(Direction d,Snake s) {
        if(d==Direction.U){
            return Direction.R;
        }else if(Direction.D==d){
            return Direction.L;
        }else if (Direction.L==d){
            return Direction.U;
        }else {
            return Direction.D;
        }
    }
}

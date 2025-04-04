public class AntiClockwise implements StrategieMouvement{
    @Override
    public Direction process(Direction d,Snake s) {
        Direction res;
        if(d==Direction.U){
            res= Direction.L;
        }else if(Direction.D==d){
            res= Direction.R;
        }else if (Direction.L==d){
            res=Direction.D;
        }else {
            res= Direction.U;
        }
        return res;
    }
}

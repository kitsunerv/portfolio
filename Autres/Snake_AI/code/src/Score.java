public class Score {
    int sec;
    int milisec;
    int apples;
    public Score(){
        sec=0;
        milisec=0;
        apples=0;
    }
    public void addTime(){
        milisec++;
        if(milisec==10){
            sec++;
            milisec=0;
        }
    }
    public void addApple(){
        apples++;
    }

    @Override
    public String toString() {
        return "Score: "+apples+" apples, "+sec+" seconds";
    }
}

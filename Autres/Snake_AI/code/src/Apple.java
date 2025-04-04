import java.util.Random;

public class Apple {
    int x,y;
    public Apple(int[][] b){
        placeNew(b);
    }

    public void placeNew(int[][] b){
        Random rd = new Random();
        int height=b.length;
        int width=b[0].length;
        y= rd.nextInt(height-4)+2;
        x = rd.nextInt(width-4)+2;
        while(b[y][x]!=0){
            y = rd.nextInt(height);
            x = rd.nextInt(width);
        }
    }
}

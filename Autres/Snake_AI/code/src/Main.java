public class Main {
    public static void main(String[] args) {
        Board b=new Board(40,20);
        while (b.status){
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println(b);
            try {
                b.snake.move(AI.move(b), b);
            }catch (ArrayIndexOutOfBoundsException e){
                System.out.println("snake went OOB");
                b.printGrille();
                b.gameOver();
            }
            b.fillBoard2();
           try {
                Thread.sleep(100);
                b.score.addTime();
            }catch (Exception e){
                System.out.println("sleep failed");
            }
        }
    }
}


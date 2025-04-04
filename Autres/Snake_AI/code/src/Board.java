public class Board {
    boolean status;
    Score score;
    int width;
    int height;
    Apple apple;
    int[][] board;
    Direction currDir;
    Snake snake;
    public Board(int width,int height){
        status=true;
        this.height=height+4;
        this.width=width+4;
        board=new int[height+4][width+4];
        currDir=Direction.U;
        score=new Score();
        snake=new Snake(4,this.width,this.height);
        fillBoard1();
        apple=new Apple(board);
        fillBoard2();
    }

    public void fillBoard1(){
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if(i<2||i>height-2||j<2||j>width-2){
                    board[i][j]=5;
                }else {
                    board[i][j]=0;
                }
            }
        }
        int y=snake.snake.get(0)[0];
        int x=snake.snake.get(0)[1];
        board[y][x]=1;
        for (int i = 1; i < snake.len; i++) {
            y=snake.snake.get(i)[0];
            x=snake.snake.get(i)[1];
            board[y][x]=2;
        }
    }
    public void fillBoard2(){
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if(i<2||i>=height-2||j<2||j>=width-2){
                    board[i][j]=5;
                }else {
                    board[i][j]=0;
                }
            }
        }
        int y=snake.snake.get(0)[0];
        int x=snake.snake.get(0)[1];
        board[y][x]=1;
        for (int i = 1; i < snake.len; i++) {
            y = snake.snake.get(i)[0];
            x = snake.snake.get(i)[1];
            board[y][x] = 2;
        }
        board[apple.y][apple.x]=9;
    }
    void gameOver(){
        this.status=false;
    }
    void printGrille(){
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                System.out.print(board[i][j]);
            }
            System.out.println("");
        }
    }
    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        for (int i = 2; i < height-2; i++) {
            for (int j = 2; j < width-2; j++) {
                if (board[i][j]==0){
                    res.append("  ");
                }else if (board[i][j]==1){
                    if (currDir==Direction.U){
                        res.append("°°");
                    }else if (currDir==Direction.D){
                        res.append("..");
                    }else if (currDir==Direction.R){
                        res.append("]:");
                    }else{
                        res.append(":[");
                    }
                }else if (board[i][j]==2){
                    res.append("[]");
                }else if (board[i][j]==9){
                    res.append("CD");
                }
            }
            res.append("|\n");
        }
        res.append("--".repeat(Math.max(0, width - 4)));
        res.append("/\n");
        res.append(score);
        return res.toString();
    }
}

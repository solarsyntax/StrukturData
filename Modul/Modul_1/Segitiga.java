import java.util.Scanner;

public class Segitiga<nilai extends Number> {
    private nilai alas;
    private nilai tinggi;

    // Constructor untuk inisialisasi nilai alas dan tinggi
    public Segitiga(nilai alas, nilai tinggi) {
        this.alas = alas;
        this.tinggi = tinggi;
    }

    // Menghitung luas segitiga dan mengembalikan hasil sebagai tipe int
    public int getResultAsInt() {
        double luas = 0.5 * alas.intValue() * tinggi.intValue();
        return (int) luas;
    }

    // Menghitung luas segitiga dan mengembalikan hasil sebagai tipe double
    public double getResultAsDouble() {
        return 0.5 * alas.doubleValue() * tinggi.doubleValue();
    }

    // Contoh penggunaan class generic Segitiga pada main
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input nilai alas dan tinggi sebagai integer
        System.out.print("Masukkan nilai alas (integer): ");
        int inputAlasInt = scanner.nextInt();
        System.out.print("Masukkan nilai tinggi (integer): ");
        int inputTinggiInt = scanner.nextInt();

        Segitiga<Integer> luasTipeInt = new Segitiga<>(inputAlasInt, inputTinggiInt);
        int hasilInt = luasTipeInt.getResultAsInt();
        System.out.println("Luas segitiga dengan input integer: " + hasilInt);

        // Input nilai alas dan tinggi sebagai double
        System.out.print("Masukkan nilai alas (double): ");
        double inputAlasDouble = scanner.nextDouble();
        System.out.print("Masukkan nilai tinggi (double): ");
        double inputTinggiDouble = scanner.nextDouble();

        Segitiga<Double> luasTipeDouble = new Segitiga<>(inputAlasDouble, inputTinggiDouble);
        double hasilDouble = luasTipeDouble.getResultAsDouble();
        System.out.println("Luas segitiga dengan input double: " + hasilDouble);
    }
}

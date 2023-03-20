package Modul.Modul_2;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> hewan = new ArrayList();
        ArrayList<String> deleteHewan = new ArrayList();

        hewan.add("Sapi");
        hewan.add("Kelinci");
        hewan.add("Kambing");
        hewan.add("Unta");
        hewan.add("Domba");

        deleteHewan.add("Kelinci");
        deleteHewan.add("Kambing");
        deleteHewan.add("Unta");

        System.out.println("Hewan : " + hewan);

        hewan.removeAll(deleteHewan);

        System.out.println("Hewan yang dihapus: " + deleteHewan);
        System.out.println("Output Hewan : " + hewan);
    }
}

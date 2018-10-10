package com.cuiods.datamining.h1.main;

import com.cuiods.datamining.h1.filter.*;

public class Main {

    public static void main(String[] args) {
        new AccountFilter().processCsv();
        new CardFilter().processCsv();
        new ClientFilter().processCsv();
        new DispFilter().processCsv();
        new DistrictFilter().processCsv();
        new LoadFilter().processCsv();
        new OrderFilter().processCsv();
        new TranFilter().processCsv();
    }


}

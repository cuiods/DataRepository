package com.cuiods.datamining.h1.util;

import com.csvreader.CsvReader;
import org.junit.Test;

import java.io.IOException;

import static org.junit.Assert.*;

public class CsvIOTest {

    @Test
    public void readCsv() {
        CsvReader reader = CsvIO.readCsv("account.csv");
        try {
            reader.readHeaders();
            int i = 0;
            while (reader.readRecord() && i < 10) {
                System.out.println(reader.getRawRecord());
                System.out.println(reader.get("account_id"));
                i++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Test
    public void writeCsv() {
    }
}
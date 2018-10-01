package com.cuiods.datamining.h1.util;

import com.csvreader.CsvReader;
import com.csvreader.CsvWriter;

import java.io.FileNotFoundException;
import java.net.URL;

public class CsvIO {


    public static CsvReader readCsv(String filePath) {
        CsvReader reader = null;
        URL pathUrl = CsvIO.class.getClassLoader().getResource(filePath);
        String path = "";
        if (pathUrl!=null) {
            path = pathUrl.getPath();
        }
        try {
            reader = new CsvReader(path);
        } catch (FileNotFoundException e) {
            System.err.println("Cannot find csv file, file path:"+ filePath);
            e.printStackTrace();
        }
        return reader;
    }

    public static CsvWriter writeCsv(String filePath) {
        URL pathUrl = CsvIO.class.getClassLoader().getResource(filePath);
        String path = "";
        if (pathUrl!=null) {
            path = pathUrl.getPath();
        }
        return new CsvWriter(path);
    }
}

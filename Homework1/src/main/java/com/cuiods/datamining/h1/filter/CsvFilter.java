package com.cuiods.datamining.h1.filter;

import com.csvreader.CsvReader;
import com.csvreader.CsvWriter;
import com.cuiods.datamining.h1.rules.Rule;
import com.cuiods.datamining.h1.util.CsvIO;

import java.io.IOException;
import java.util.List;

public abstract class CsvFilter {

    abstract String getCsvName();
    abstract List<Rule> getRules();

    public void processCsv() {
        CsvReader reader = CsvIO.readCsv(getCsvName()+".csv");
        CsvWriter writer = CsvIO.writeCsv(getCsvName()+"_new.csv");
        List<Rule> rules = getRules();
        try {
            String[] headers = reader.getHeaders();
            int itemSize = headers.length;
            writer.writeRecord(headers);
            if (itemSize != rules.size()) {
                System.err.println("Csv headers not equal to rule size");
                return;
            }
            loop:while (reader.readRecord()) {
                String[] result = new String[itemSize];
                for (int i = 0; i < itemSize; i++) {
                    String resultItem = rules.get(i).process(reader.get(headers[i]));
                    if (resultItem == null) continue loop;
                    result[i] = resultItem;
                }
                writer.writeRecord(result);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            writer.close();
        }
    }

}

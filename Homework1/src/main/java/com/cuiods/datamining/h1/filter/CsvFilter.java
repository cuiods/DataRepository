package com.cuiods.datamining.h1.filter;

import com.csvreader.CsvReader;
import com.csvreader.CsvWriter;
import com.cuiods.datamining.h1.rules.Rule;
import com.cuiods.datamining.h1.util.CsvIO;

import java.io.IOException;
import java.util.List;

public abstract class CsvFilter {

    public static final String SPLIT_TAG = "@@";

    abstract String getCsvName();
    abstract List<Rule> getRules();
    abstract String[] getHeaders();

    public void processCsv() {
        CsvReader reader = CsvIO.readCsv(getCsvName()+".csv");
        CsvWriter writer = CsvIO.writeCsv(getCsvName()+"_new.csv");
        CsvWriter error = CsvIO.writeCsv(getCsvName()+"_err.csv");
        List<Rule> rules = getRules();
        try {
            reader.readHeaders();
            String[] headers = reader.getHeaders();
            int itemSize = headers.length;
            writer.writeRecord(getHeaders());
            error.writeRecord(getHeaders());
            if (itemSize != rules.size()) {
                System.err.println("Csv headers not equal to rule size");
                return;
            }
            loop:while (reader.readRecord()) {
                int addIndex = getRules().size();
                String[] result = new String[getHeaders().length];
                for (int i = 0; i < itemSize; i++) {
                    String resultItem = rules.get(i).process(reader.get(headers[i]));
                    if (resultItem == null) {
                        error.write(reader.getRawRecord());
                        continue loop;
                    }
                    if (resultItem.contains(SPLIT_TAG)) {
                        String[] resultItems = resultItem.split(SPLIT_TAG);
                        result[i] = resultItems[0];
                        int j = 1;
                        for (; j < resultItems.length; j++) {
                            result[addIndex+j-1] = resultItems[j];
                        }
                        addIndex += j-1;
                    } else {
                        result[i] = resultItem;
                    }
                }
                writer.writeRecord(result);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            writer.close();
            error.close();
        }
    }

}

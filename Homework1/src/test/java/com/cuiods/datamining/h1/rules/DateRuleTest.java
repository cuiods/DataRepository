package com.cuiods.datamining.h1.rules;

import com.csvreader.CsvReader;
import com.cuiods.datamining.h1.util.CsvIO;
import org.junit.Test;

import java.io.IOException;

import static org.junit.Assert.*;

public class DateRuleTest {

    @Test
    public void process() {
        CsvReader reader = CsvIO.readCsv("account.csv");
        DateRule rule = new AccountDateRule();
        try {
            reader.readHeaders();
            int i = 0;
            while (reader.readRecord() && i < 10) {
                System.out.println(rule.process(reader.get("date")));
                i++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
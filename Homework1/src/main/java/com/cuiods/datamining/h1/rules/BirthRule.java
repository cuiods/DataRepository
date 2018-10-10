package com.cuiods.datamining.h1.rules;

import com.cuiods.datamining.h1.filter.CsvFilter;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class BirthRule extends Rule {
    @Override
    public String process(String item) {
        try {
            if (item.length() == 6) {
                int isMale = 1;
                int month = Integer.parseInt(item.substring(2,4));
                if (month > 50) {
                    month -= 50;
                    isMale = 0;
                }
                Calendar calendar = Calendar.getInstance();
                calendar.set(Integer.parseInt("19"+item.substring(0,2)),month,Integer.parseInt(item.substring(4)));
                SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
                String date = format.format(calendar.getTime());
                int age = 2000-calendar.get(Calendar.YEAR);
                int ageType = age/10;
                if (ageType > 6) ageType = 6;
                return date + CsvFilter.SPLIT_TAG + isMale + CsvFilter.SPLIT_TAG + age + CsvFilter.SPLIT_TAG + ageType;
            }
        } catch (Exception e) {
            return null;
        }
        return null;
    }
}

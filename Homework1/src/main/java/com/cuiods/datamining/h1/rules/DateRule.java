package com.cuiods.datamining.h1.rules;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public abstract class DateRule extends Rule {

    @Override
    public String process(String item) {
        String dateFormat = getFormat();
        DateFormat format = new SimpleDateFormat(dateFormat, Locale.getDefault());
        DateFormat toFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault());
        try {
            Date date = format.parse(item);
            return toFormat.format(date);
        } catch (ParseException e) {
            System.err.println("Date format exception: date-"+item);
        }
        return null;
    }

    abstract String getFormat();
}

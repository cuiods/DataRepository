package com.cuiods.datamining.h1.rules;

public class DurationRule extends Rule {
    @Override
    public String process(String item) {
        try {
            int num = Integer.parseInt(item);
            if (num % 12 == 0) return item;
            return null;
        } catch (Exception e) {
            return null;
        }
    }
}

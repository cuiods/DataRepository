package com.cuiods.datamining.h1.rules;

public class BankRule extends Rule {
    @Override
    public String process(String item) {
        if (item.length() == 2) return item;
        return null;
    }
}

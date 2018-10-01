package com.cuiods.datamining.h1.rules;

public class IdRule extends Rule {

    public String process(String item) {
        if (item != null && !item.isEmpty()) {
            try {
                Integer.parseInt(item);
                return item;
            } catch (NumberFormatException e) {
                return null;
            }
        }
        return null;
    }
}

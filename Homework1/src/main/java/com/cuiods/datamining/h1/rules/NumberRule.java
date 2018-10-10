package com.cuiods.datamining.h1.rules;

public class NumberRule extends Rule {
    @Override
    public String process(String item) {
        if (isNumeric(item)) {
            return item;
        }
        return null;
    }

    public static boolean isNumeric(String str){
        for (int i = str.length();--i>=0;){
            if (!Character.isDigit(str.charAt(i))){
                return false;
            }
        }
        return true;
    }
}

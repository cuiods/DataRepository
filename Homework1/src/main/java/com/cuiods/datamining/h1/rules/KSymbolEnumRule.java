package com.cuiods.datamining.h1.rules;

import java.util.Arrays;
import java.util.List;

public class KSymbolEnumRule extends EnumRule {
    @Override
    List<String> acceptStrings() {
        return Arrays.asList("POJISTNE","SIPO","LEASING","UVER","");
    }

    @Override
    List<String> replaceStrings() {
        return Arrays.asList("INSURANCE","MANAGEMENT","RENTAL","LOAN","");
    }
}

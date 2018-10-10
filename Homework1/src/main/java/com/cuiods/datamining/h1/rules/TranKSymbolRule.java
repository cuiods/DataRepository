package com.cuiods.datamining.h1.rules;

import java.util.Arrays;
import java.util.List;

public class TranKSymbolRule extends EnumRule {
    @Override
    List<String> acceptStrings() {
        return Arrays.asList("POJISTNE","SLUZBY","UROK","SANKC.UROK","SIPO","DUCHOD","UVER","");
    }

    @Override
    List<String> replaceStrings() {
        return Arrays.asList("INSURANCE","BILL","INTEREST_INCOME","INTEREST_PENALTY","HOUSEHOLD","OLD_AGE_PENSION","LOAN","");
    }
}

package com.cuiods.datamining.h1.rules;

import java.util.Arrays;
import java.util.List;

public class TranTypeRule extends EnumRule {
    @Override
    List<String> acceptStrings() {
        return Arrays.asList("PRIJEM","VYDAJ");
    }

    @Override
    List<String> replaceStrings() {
        return Arrays.asList("DEPOSIT","WITHDRAW");
    }
}

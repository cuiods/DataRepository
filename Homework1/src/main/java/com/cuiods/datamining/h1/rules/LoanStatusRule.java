package com.cuiods.datamining.h1.rules;

import java.util.Arrays;
import java.util.List;

public class LoanStatusRule extends EnumRule {
    @Override
    List<String> acceptStrings() {
        return Arrays.asList("A","B","C","D");
    }

    @Override
    List<String> replaceStrings() {
        return Arrays.asList("A","B","C","D");
    }
}

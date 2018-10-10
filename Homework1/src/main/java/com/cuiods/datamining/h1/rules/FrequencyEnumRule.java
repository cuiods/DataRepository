package com.cuiods.datamining.h1.rules;

import java.util.Arrays;
import java.util.List;

public class FrequencyEnumRule extends EnumRule {
    @Override
    List<String> acceptStrings() {
        return Arrays.asList("POPLATEK MESICNE", "POPLATEK TYDNE", "POPLATEK PO OBRATU");
    }

    @Override
    List<String> replaceStrings() {
        return Arrays.asList("ONCE A MONTH", "ONCE A WEEK", "AFTER DEAL");
    }
}

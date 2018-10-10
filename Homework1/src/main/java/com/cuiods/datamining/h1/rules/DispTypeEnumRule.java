package com.cuiods.datamining.h1.rules;

import java.util.Arrays;
import java.util.List;

public class DispTypeEnumRule extends EnumRule {
    @Override
    List<String> acceptStrings() {
        return Arrays.asList("OWNER","DISPONENT");
    }

    @Override
    List<String> replaceStrings() {
        return Arrays.asList("OWNER","DISPONENT");
    }
}

package com.cuiods.datamining.h1.rules;

import java.util.Arrays;
import java.util.List;

public class CardTypeEnumRule extends EnumRule {
    @Override
    List<String> acceptStrings() {
        return Arrays.asList("junior","classic","gold");
    }

    @Override
    List<String> replaceStrings() {
        return Arrays.asList("JUNIOR","CLASSIC","GOLD");
    }
}

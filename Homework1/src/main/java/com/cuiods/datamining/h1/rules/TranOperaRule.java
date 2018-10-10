package com.cuiods.datamining.h1.rules;

import java.util.Arrays;
import java.util.List;

public class TranOperaRule extends EnumRule {
    @Override
    List<String> acceptStrings() {
        return Arrays.asList("VYBER KARTOU","VKLAD","PREVOD Z UCTU","VYBER","PREVOD NA UCET");
    }

    @Override
    List<String> replaceStrings() {
        return Arrays.asList("CREDIT_WITHDRAW","CREDIT_CASH","FROM_OTHER_BANK","CASH","TO_OTHER_BANK");
    }
}

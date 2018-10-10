package com.cuiods.datamining.h1.rules;

public class AccountDateRule extends DateRule {
    @Override
    String getFormat() {
        return "yyyy/MM/dd H:mm";
    }
}

package com.cuiods.datamining.h1.rules;

public class TranDateRule extends DateRule {
    @Override
    String getFormat() {
        return "yyyy-MM-dd HH:mm:ss";
    }
}

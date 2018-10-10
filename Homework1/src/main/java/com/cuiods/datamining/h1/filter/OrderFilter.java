package com.cuiods.datamining.h1.filter;

import com.cuiods.datamining.h1.rules.*;

import java.util.ArrayList;
import java.util.List;

public class OrderFilter extends CsvFilter {
    @Override
    String getCsvName() {
        return "order";
    }

    @Override
    List<Rule> getRules() {
        List<Rule> rules = new ArrayList<Rule>(6);
        rules.add(new IdRule());
        rules.add(new IdRule());
        rules.add(new BankRule());
        rules.add(new NumberRule());
        rules.add(new NumberRule());
        rules.add(new KSymbolEnumRule());
        return rules;
    }

    @Override
    String[] getHeaders() {
        return new String[]{"order_id","account_id","bank_to","account_to","amount","k_symbol"};
    }
}

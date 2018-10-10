package com.cuiods.datamining.h1.filter;

import com.cuiods.datamining.h1.rules.*;

import java.util.ArrayList;
import java.util.List;

public class LoadFilter extends CsvFilter {
    @Override
    String getCsvName() {
        return "loan";
    }

    @Override
    List<Rule> getRules() {
        List<Rule> rules = new ArrayList<Rule>(8);
        rules.add(new IdRule());
        rules.add(new IdRule());
        rules.add(new AccountDateRule());
        rules.add(new NumberRule());
        rules.add(new DurationRule());
        rules.add(new NumberRule());
        rules.add(new LoanStatusRule());
        rules.add(new NumberRule());
        return rules;
    }

    @Override
    String[] getHeaders() {
        return new String[]{"loan_id","account_id","date","amount","duration","payments","status","payduration"};
    }
}

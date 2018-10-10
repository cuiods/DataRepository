package com.cuiods.datamining.h1.filter;

import com.cuiods.datamining.h1.rules.BirthRule;
import com.cuiods.datamining.h1.rules.IdRule;
import com.cuiods.datamining.h1.rules.Rule;

import java.util.ArrayList;
import java.util.List;

public class ClientFilter extends CsvFilter {
    @Override
    String getCsvName() {
        return "client";
    }

    @Override
    List<Rule> getRules() {
        List<Rule> rules = new ArrayList<Rule>(3);
        rules.add(new IdRule());
        rules.add(new BirthRule());
        rules.add(new IdRule());
        return rules;
    }

    @Override
    String[] getHeaders() {
        return new String[]{"client_id","birth_number","district_id","gender","age", "ageType"};
    }
}

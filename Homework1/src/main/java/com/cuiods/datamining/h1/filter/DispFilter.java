package com.cuiods.datamining.h1.filter;

import com.cuiods.datamining.h1.rules.DispTypeEnumRule;
import com.cuiods.datamining.h1.rules.IdRule;
import com.cuiods.datamining.h1.rules.Rule;

import java.util.ArrayList;
import java.util.List;

public class DispFilter extends CsvFilter {
    @Override
    String getCsvName() {
        return "disp";
    }

    @Override
    List<Rule> getRules() {
        List<Rule> rules = new ArrayList<Rule>(4);
        rules.add(new IdRule());
        rules.add(new IdRule());
        rules.add(new IdRule());
        rules.add(new DispTypeEnumRule());
        return rules;
    }

    @Override
    String[] getHeaders() {
        return new String[]{"disp_id","client_id","account_id","type"};
    }
}

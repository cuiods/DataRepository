package com.cuiods.datamining.h1.filter;

import com.cuiods.datamining.h1.rules.AccountDateRule;
import com.cuiods.datamining.h1.rules.FrequencyEnumRule;
import com.cuiods.datamining.h1.rules.IdRule;
import com.cuiods.datamining.h1.rules.Rule;

import java.util.ArrayList;
import java.util.List;

public class AccountFilter extends CsvFilter {

    @Override
    String getCsvName() {
        return "account";
    }

    @Override
    List<Rule> getRules() {
        List<Rule> rules = new ArrayList<Rule>(4);
        rules.add(new IdRule());
        rules.add(new IdRule());
        rules.add(new FrequencyEnumRule());
        rules.add(new AccountDateRule());
        return rules;
    }

    @Override
    String[] getHeaders() {
        return new String[]{"account_id","district_id","frequency","date"};
    }
}

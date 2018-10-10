package com.cuiods.datamining.h1.filter;

import com.cuiods.datamining.h1.rules.AccountDateRule;
import com.cuiods.datamining.h1.rules.CardTypeEnumRule;
import com.cuiods.datamining.h1.rules.IdRule;
import com.cuiods.datamining.h1.rules.Rule;

import java.util.ArrayList;
import java.util.List;

public class CardFilter extends CsvFilter {
    @Override
    String getCsvName() {
        return "card";
    }

    @Override
    List<Rule> getRules() {
        List<Rule> rules = new ArrayList<Rule>(4);
        rules.add(new IdRule());
        rules.add(new IdRule());
        rules.add(new CardTypeEnumRule());
        rules.add(new AccountDateRule());
        return rules;
    }

    @Override
    String[] getHeaders() {
        return new String[]{"card_id","disp_id","type","issued"};
    }
}

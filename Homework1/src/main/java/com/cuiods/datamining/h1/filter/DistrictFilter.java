package com.cuiods.datamining.h1.filter;

import com.cuiods.datamining.h1.rules.IdRule;
import com.cuiods.datamining.h1.rules.NumberRule;
import com.cuiods.datamining.h1.rules.Rule;
import com.cuiods.datamining.h1.rules.StringRule;

import java.util.ArrayList;
import java.util.List;

public class DistrictFilter extends CsvFilter {
    @Override
    String getCsvName() {
        return "district";
    }

    @Override
    List<Rule> getRules() {
        List<Rule> rules = new ArrayList<Rule>(8);
        rules.add(new IdRule());
        rules.add(new StringRule());
        rules.add(new StringRule());
        rules.add(new NumberRule());
        rules.add(new NumberRule());
        rules.add(new NumberRule());
        rules.add(new StringRule());
        rules.add(new NumberRule());
        return rules;
    }

    @Override
    String[] getHeaders() {
        return new String[]{"district_id","district_name","region","hab_number","city_number","ave_salary"
                ,"umemploy_rate","crime_number"};
    }
}

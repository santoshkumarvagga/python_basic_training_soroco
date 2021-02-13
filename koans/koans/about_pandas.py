#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

from runner.koan import *


class AboutPandas(Koan):
    """
    To quickly learn Pandas basics, refer : http://pandas.pydata.org/pandas-docs/stable/10min.html

    a more detailed tutorial as ipython notebooks: https://github.com/PacktPublishing/Pandas-Cookbook
    """
    employees = pd.DataFrame(columns=['name', 'age', 'employee_id', 'email', 'phone_number', 'country'],
                             data=[['Ramesh', 25, 'EMP001', 'ramesh@company.com', '9456123781', 'India'],
                                   ['Suresh', 27, 'EMP002', 'suresh@company.com', '7586549812', 'India'],
                                   ['Parker', 24, 'EMP003', 'parker@company.com', '1234567891', 'USA'],
                                   ['John', 29, 'EMP004', 'john@company.com', '176512349876', 'USA']
                                   ])

    def test_filtering_dataframe(self) -> None:
        """
        retrieve all the rows that satisfy given condition.

        1. in here we construct a truth value Series:
            a pandas series with indexes and True for satisfying rows and False for others.

        2. we pass the above series and required column names to '.loc' api, which gives us data rows that satisfy
        specified conditions and having the specified columns

        Ex: extract all the employees aged above 25

        it is recommended to filter data sets using Series operations as they are vectorised and fast.
        running below filter on a million rows might take 5 to 10 seconds max.

        Returns:
            None
        """

        # constructing a truth value Series for required condition
        filter_age_gt_25 = self.employees['age'] > 25

        # we use the above filter and run on actual DataFrame and also take the required column and convert it to list
        employees_above_25 = self.employees.loc[filter_age_gt_25, 'name'].tolist()

        self.assertEqual(employees_above_25, [__])

    def test_filtering_dataframe_2(self) -> None:
        """
        extract all the employees from USA

        Returns:
            None
        """

        # constructing a truth value Series for required condition
        filter_us_employees = __

        # we use the above filter and run on actual DataFrame and also take the required column and convert it to list
        employees_in_us = self.employees.loc[filter_us_employees, 'name'].tolist()

        self.assertEqual(employees_in_us, ['Parker', 'John'])

    def test_combine_filters(self) -> None:
        """
        we can combine filters using bitwise '&' and '|' operators. to inverse use '~'
        ex: extract all the employees aged above 25 and are based in 'India'

        Returns:
            None
        """
        # filter out indian employees aged above 25 years
        filter_age_gt_25 = __
        filter_from_india = __

        indian_employees_above_25 = self.employees.loc[filter_age_gt_25 & filter_from_india, 'name'].tolist()
        self.assertEqual(indian_employees_above_25, ['Suresh'])

    def test_filter_and_update_all(self) -> None:
        """
        update all the rows satisfying certain condition.

        Group Updates are also quick

        ex: Move all the Indian employees to Australia

        Note: Always use '.loc',
              watch out for SettingWithCopyWarning 'https://www.dataquest.io/blog/settingwithcopywarning/'

        Returns:
            None
        """
        employees = pd.DataFrame(columns=['name', 'age', 'employee_id', 'email', 'phone_number', 'country'],
                                 data=[['Ramesh', 25, 'EMP001', 'ramesh@company.com', '9456123781', 'India'],
                                       ['Suresh', 27, 'EMP002', 'suresh@company.com', '7586549812', 'India'],
                                       ['Parker', 24, 'EMP003', 'parker@company.com', '1234567891', 'USA'],
                                       ['John', 29, 'EMP003', 'john@company.com', '176512349876', 'USA']
                                       ])

        employees.loc[employees['country'] == 'India', 'country'] = 'Australia'

        australian_employees = employees.loc[employees['country'] == 'Australia', 'name'].tolist()

        self.assertEqual(australian_employees, [__])

    def test_filter_and_update_group(self) -> None:
        """
        update all the rows satisfying certain condition.

        Group Updates are also quick

        ex: update country code column based on country names for all the employees, fill the blanks

        Note: Always use '.loc',
              watch out for SettingWithCopyWarning 'https://www.dataquest.io/blog/settingwithcopywarning/'

        Returns:
            None
        """
        employees = pd.DataFrame(columns=['name', 'age', 'employee_id', 'email', 'phone_number', 'country',
                                          'country_code'],
                                 data=[['Ramesh', 25, 'EMP001', 'ramesh@company.com', '9456123781', 'India', ''],
                                       ['Suresh', 27, 'EMP002', 'suresh@company.com', '7586549812', 'India', ''],
                                       ['Parker', 24, 'EMP003', 'parker@company.com', '1234567891', 'USA', ''],
                                       ['John', 29, 'EMP003', 'john@company.com', '176512349876', 'USA', '']
                                       ])

        employees_expected = pd.DataFrame(columns=['name', 'age', 'employee_id', 'email', 'phone_number', 'country',
                                                   'country_code'],
                                 data=[['Ramesh', 25, 'EMP001', 'ramesh@company.com', '9456123781', 'India', '91'],
                                       ['Suresh', 27, 'EMP002', 'suresh@company.com', '7586549812', 'India', '91'],
                                       ['Parker', 24, 'EMP003', 'parker@company.com', '1234567891', 'USA', '1'],
                                       ['John', 29, 'EMP003', 'john@company.com', '176512349876', 'USA', '1']
                                       ])

        # TODO EXERCISE: ADD COUNTRY CODES TO EMPLOYEES DF BASED ON COUNTRY NAMES
        employees.loc[employees['country'] == __, __] = ___

        for index, row in employees_expected.iterrows():
            # PLEASE FILL IN THE ABOVE TEMPLATE, AND ADD REQUIRED CODE FOR ASSERT TO PASS
            self.assertEqual(employees.loc[index]['country_code'], row['country_code'])

    def test_filter_and_update_each_row(self) -> None:
        """
        modify each row, based on some data/criteria in the same row

        Note: using 'apply' api is a lot slower when compared to vectorised modification done above.
            not a matter if scale is not a concern

            apply does not modify the DataFrame inplace it gives out the modified DataFrame

        Returns:
            None
        """
        def change_email_extension(row: pd.Series) ->pd.Series:
            """
            function for apply: runs for each row,

            ex: add country code extension to email ids based on their country for each employee.

            Args:
                row: current data row

            Returns:
                modified row
            """
            splited_id = row['email'].split('@')

            extension = ''

            if row['country'] == 'India':
                extension = 'in.'

            if row['country'] == 'USA':
                extension = 'us.'

            row['email'] = "{unique_id}@{extension}{domain}".format(unique_id=splited_id[0],
                                                                    extension=extension,
                                                                    domain=splited_id[1])
            return row

        # expected DataFrame after applying the changes
        expected_df = pd.DataFrame(columns=['name', 'age', 'employee_id', 'email', 'phone_number', 'country'],
                                   data=[
                                       ['Ramesh', 25, 'EMP001', 'ramesh@in.company.com', '9456123781', 'India'],
                                       ['Suresh', 27, 'EMP002', 'suresh@in.company.com', '7586549812', 'India'],
                                       ['Parker', 24, 'EMP003', 'parker@us.company.com', '1234567891', 'USA'],
                                       ['John', 29, 'EMP004', 'john@us.company.com', '176512349876', 'USA']
                                       ])

        # Applies the given function to reach row and returns modifed DataFrame
        modified_df = self.employees.apply(change_email_extension, axis=1)

        # asert if modified employee email ids match with expected email ids
        for index, row in modified_df.iterrows():

            # select the modified_df's row that has the current row name
            condition_names_matching = (expected_df['name'] == row['name'])

            # '.loc' always returns a Series, so we will retrieve the first value
            expected_email_id = expected_df.loc[condition_names_matching, 'email'].values[0]

            # assert if current row's email id is same as its expected email id
            self.assertEqual(__, expected_email_id)

    def test_filter_and_update_each_row_2(self) -> None:
        """
        modify each row, based on some data/criteria in the same row

        Note: using 'apply' api is a lot slower when compared to vectorised modification done above.
            not a matter if scale is not a concern

            apply does not modify the DataFrame inplace it gives out the modified DataFrame

        Returns:
            None
        """
        def add_country_codes(row : pd.Series) ->pd.Series:
            """
            function for apply: runs for each row,

            ex: add country telephone code extension to phone numbers based on their country for each employee.
                91 for indians and 1 for americans

            Args:
                row: current data row

            Returns:
                modified row
            """

            # TODO EXERCISE: ADD CODE TO INCLUDE CONTRY CODE IN PHONENUMBER

            return row

        # expected DataFrame after applying the changes
        expected_df = pd.DataFrame(columns=['name', 'age', 'employee_id', 'email', 'phone_number', 'country'],
                                   data=[
                                       ['Ramesh', 25, 'EMP001', 'ramesh@company.com', '919456123781', 'India'],
                                       ['Suresh', 27, 'EMP002', 'suresh@company.com', '917586549812', 'India'],
                                       ['Parker', 24, 'EMP003', 'parker@company.com', '11234567891', 'USA'],
                                       ['John', 29, 'EMP004', 'john@company.com', '1176512349876', 'USA']
                                       ])

        # Applies the given function to reach row and returns modifed DataFrame
        modified_df = self.employees.apply(add_country_codes, axis=1)

        # asert if modified employee email ids match with expected email ids
        for index, row in modified_df.iterrows():

            # retrieve the phone number expected
            expected_phone_number = expected_df.loc[expected_df['name'] == row['name'], 'phone_number'].values[0]

            # assert if current row's email id is same as its expected email id
            # PLEASE ADD THE CODE IN 'add_country_codes' METHOD, FOR ASSERT TO PASS
            self.assertEqual(row['phone_number'], expected_phone_number)

    def test_search_substring_match(self)-> None:
        """
        Get employee names having '123' in their phone number

        Note: 'contains' searches are bit slow when dealing with large number of rows

        Returns:
            None
        """
        search_filter = self.employees['phone_number'].str.contains('123')

        employees_having_123_in_phone_number = self.employees.loc[search_filter, 'name'].tolist()

        self.assertEqual(employees_having_123_in_phone_number, [__])

    def test_search_substring_match_2(self)-> None:
        """
        Get employee names ending with 'esh' in their phone number

        Note: 'contains' searches are bit slow when dealing with large number of rows

        Returns:
            None
        """
        search_filter = __

        employee_names_ending_with_esh = self.employees.loc[search_filter, 'name'].tolist()

        self.assertEqual(employee_names_ending_with_esh, ['Ramesh', 'Suresh'])

    def test_search_for_a_list_of_matches(self) -> None:
        """
        Get employee names of the employee_ids in given list

        Returns:
            None
        """
        search_filter = self.employees['employee_id'].isin(['EMP001', 'EMP003', 'EMP002'])

        names_of_employees = self.employees.loc[search_filter, 'name'].tolist()

        self.assertEqual(names_of_employees, [__])

    def test_grouping_data(self) -> None:
        """
        get country wise list of employees

        Returns:
            None
        """
        grouped_country = self.employees.groupby(by=['country'])

        for country, group in grouped_country:

            names = group['name'].tolist()

            if country == 'India':
                self.assertEqual(names, [__])

            if country == 'USA':
                self.assertEqual(names, [__])

    def test_merge_dataframes(self) -> None:
        """
        using 'employee' and 'employee_details' DF's retrieve list of manager id's managing all the indian employees's

        Returns:
            None
        """
        employee_details = pd.DataFrame(columns=['emp_id', 'Joining_date', 'cost_center', 'manager_id', 'band'],
                                        data=[
                                            ['EMP001', '09/01/2014', 'IJR', 'mahesh@company.com', 'B5'],
                                            ['EMP002', '31/06/2016', 'IPR', 'manish@company.com', 'B7'],
                                            ['EMP003', '12/05/2014', 'UJR', 'irina@company.com', 'M10'],
                                            ['EMP004', '21/06/2016', 'UPR', 'richerd@company.com', 'B8']
                                        ])

        merged_df = self.employees.merge(employee_details, left_on=['employee_id'], right_on=['emp_id'], how='inner')

        filter_indian_employees = merged_df['country'] == 'India'

        managers_for_indian_employees = merged_df.loc[filter_indian_employees, 'manager_id'].tolist()

        self.assertEqual(managers_for_indian_employees, [__])

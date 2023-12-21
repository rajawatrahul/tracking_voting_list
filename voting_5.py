# Voting_Program_1
import pandas as pd
import streamlit as st



def voting_data_s():
    dfs = pd.read_csv('Data_list.csv')
    p = st.selectbox('Polling Station', dfs.Place.unique())
    df = dfs[dfs['Place'] == p]
    tt = len(df[df['Place'] == p])
    ma = len(df[(df['Place'] == p) & (df['Gender'] == 'M')])
    fe = len(df[(df['Place'] == p) & (df['Gender'] == 'F')])
    if p != ' ':
        st.write('Total=', tt, 'Male=', ma, 'Female=', fe)
        options = ['', 'Caste', 'Profession', 'Generation', 'Caste+Age']
        opt = st.selectbox('Option', options)
        if opt == '':
            st.write('')
        elif opt == 'Caste':
            pp = df[df['Place'] == p].groupby('Caste').size().to_frame('Total') \
                .sort_values('Total', ascending=False)
            pp['Perc%'] = ((pp['Total'] / tt) * 100).astype('int')
            pp.reset_index(inplace=True)
            pp.index = pp.index + 1
            st.dataframe(pp, width=500)
        elif opt == 'Profession':
            pp = df[df['Place'] == p].groupby('Profession').size().to_frame('Total') \
                .sort_values('Total', ascending=False)
            pp['Perc%'] = ((pp['Total'] / tt) * 100).astype('int')
            pp.reset_index(inplace=True)
            pp.index = pp.index + 1
            st.dataframe(pp, width=500)
        elif opt == 'Generation':
            values = st.slider('Select a range of values', 18, 130, (18, 130))
            pp = df[(df['Place'] == p) & (df['Age'].between(values[0], values[1]))].groupby(
                'Age').size().to_frame('Total') \
                .sort_values('Total', ascending=False)
            pp['Perc%'] = ((pp['Total'] / tt) * 100).astype('int')
            pp.reset_index(inplace=True)
            pp.index = pp.index + 1
            st.dataframe(pp, width=500)
        elif opt == 'Caste+Age':
            values = st.slider('Select a range of values', 18, 130, (18, 130))
            pp = df[(df['Place'] == p) & (df['Age'].between(values[0], values[1]))].groupby(
                ['Caste', 'Age']).size().to_frame('Total') \
                .sort_values('Age', ascending=True)
            # pp['Perc%'] = ((pp['Total'] / tt) * 100).astype('int')
            pp.reset_index(inplace=True)
            pp.index = pp.index + 1
            st.dataframe(pp, width=500)


def voting_data_r():
    dfr = pd.read_csv('Data_list.csv')
    # t = len(dfr.index)
    options = ['', 'Caste', 'Profession', 'Generation']
    opt = st.selectbox('Option', options)
    if opt == 'Caste':
        na_list = dfr.Caste.unique().tolist()
        na_list.sort()
        na_list = [''] + na_list
        oppt = st.selectbox('Choice', na_list)
        if oppt != '':
            pp = dfr[dfr['Caste'] == oppt].groupby('Place').size().to_frame('Total') \
                .sort_values('Total', ascending=False)
            s = pp['Total'].sum()
            pp['Perc%'] = ((pp['Total'] / s) * 100).astype('int')
            pp.reset_index(inplace=True)
            pp.index = pp.index + 1
            st.dataframe(pp, width=500)
    elif opt == 'Profession':
        na_list = dfr.Profession.unique().tolist()
        na_list.sort()
        na_list = [''] + na_list
        oppt = st.selectbox('Choice', na_list)
        if oppt != '':
            pp = dfr[dfr['Profession'] == oppt].groupby('Place').size().to_frame('Total') \
                .sort_values('Total', ascending=False)
            s = pp['Total'].sum()
            pp['Perc%'] = ((pp['Total'] / s) * 100).astype('int')
            pp.reset_index(inplace=True)
            pp.index = pp.index + 1
            st.dataframe(pp, width=500)
    elif opt == 'Generation':
        values = st.slider('Select a range of values', 18, 130, (18, 130))
        pp = dfr[(dfr['Age'].between(values[0], values[1]))].groupby('Place').size() \
            .to_frame('Total').sort_values('Total', ascending=False)
        s = pp['Total'].sum()
        pp['Perc%'] = ((pp['Total'] / s) * 100).astype('int')
        pp.reset_index(inplace=True)
        pp.index = pp.index + 1
        st.dataframe(pp, width=500)


def voting_data_l():
    dff = pd.read_csv('Data_list.csv')
    p = st.selectbox('Polling Station', dff.Place.unique())
    df = dff[dff['Place'] == p]
    # st.write(dff)
    if p != ' ':
        options = ['', 'Caste', 'Profession', 'Generation']
        opt = st.selectbox('Option', options)
        st.write(opt)
        if opt == 'Caste':
            na_list = df.Caste.unique().tolist()
            na_list.sort()
            na_list = [''] + na_list
            pp = st.selectbox('Choice', na_list)
            qq = (df[df['Caste'] == pp])
            rr = qq.loc[:, 'Sr.No': 'Father/Husband'].reset_index(drop=True)
            rr.index = rr.index + 1
            # rr = rr.set_index('Sr.No')
            st.table(rr)
        elif opt == 'Profession':
            na_list = df.Profession.unique().tolist()
            na_list.sort()
            na_list = [''] + na_list
            pp = st.selectbox('Choice', na_list)
            qq = (df[df['Profession'] == pp])
            rr = qq.loc[:, 'Sr.No': 'Father/Husband'].reset_index(drop=True)
            rr.index = rr.index + 1
            # rr = rr.set_index('Sr.No')
            st.table(rr)
        elif opt == 'Generation':
            values = st.slider('Select a range of values', 18, 130, (18, 130))
            pp = df[df['Age'].between(values[0], values[1])]
            qq = pp.loc[:, 'Sr.No': 'Father/Husband'].reset_index(drop=True)
            qq.index = qq.index + 1
            st.table(qq)


if __name__ == '__main__':
    status = st.sidebar.radio('Start', ('Straight_Counting', 'Reverse_Counting', 'Direct_Voting_List'))
    if status == 'Straight_Counting':
        voting_data_s()
    elif status == 'Reverse_Counting':
        voting_data_r()
    # elif status == 'Direct_Voting_List':
    #    voting_data_l()

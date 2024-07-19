def identify_high_risk_permissions(df):
    high_risk_permissions = ['iam.serviceAccounts.create', 'resourcemanager.projects.delete']
    df['high_risk'] = df['permissions'].apply(lambda perms: any(perm in perms for perm in high_risk_permissions))
    return df[df['high_risk']]

high_risk_df = identify_high_risk_permissions(iam_df)

def groups_with_many_permissions(df):
    groups_df = df[df['member'].str.contains('group:')]
    group_permissions_count = groups_df.groupby('member')['permissions'].apply(lambda perms: len(set([item for sublist in perms for item in sublist])))
    return group_permissions_count.sort_values(ascending=False)

groups_permissions_df = groups_with_many_permissions(iam_df)

# Save the analysis to CSV files
high_risk_df.to_csv('high_risk_permissions.csv', index=False)
groups_permissions_df.to_csv('groups_permissions_count.csv')

// 1279F - New Year And Handle Change

// Great example of the "Aliens Trick" - DP optimization

// dp[i] = max(dp[i-1] + s[i], (i + 1 - max(i-l+1, 0)) + dp[i-l] - lambda)

#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

char *readline();
char *ltrim(char *);
char *rtrim(char *);
char **split_string(char *);

typedef struct dp_val
{
    int val;
    int cnt;
} dp_val;

int max(int a, int b)
{
    return (a > b) ? a : b;
}

int min(int a, int b)
{
    return (a < b) ? a : b;
}

int compute_dp(int n, int *dp_table, int *cnt_table, int l, char *s, int theta)
{
    int i = 0;
    while (i < n)
    {
        int a = (i - 1 < 0) ? 0 : dp_table[i - 1];
        a += (s[i] == '1') ? 1 : 0;
        int a_cnt = (i - 1 < 0) ? 0 : cnt_table[i - 1];
        int b = (i - l < 0) ? 0 : dp_table[i - l];
        b += (i + 1 - max(i - l + 1, 0)) - theta;
        int b_cnt = (i - l < 0) ? 0 : cnt_table[i - l];
        b_cnt += 1;
        if (a >= b)
        {
            dp_table[i] = a;
            cnt_table[i] = a_cnt;
        }
        else
        {
            dp_table[i] = b;
            cnt_table[i] = b_cnt;
        }
        i++;
    }
    return 0;
}

int binary_search(int n, int k, int l, char *s, int *dp_table, int *cnt_table)
{
    int low = 0;
    int high = l + 1;
    int theta;
    while (low < high)
    {
        theta = (low + high) / 2;
        compute_dp(n, dp_table, cnt_table, l, s, theta);
        if (cnt_table[n - 1] == k)
        {
            return theta;
        }
        else if (cnt_table[n - 1] > k)
        {
            low = theta + 1;
        }
        else
        {
            high = theta;
        }
    }
    return low;
}

int main()
{
    char **inp = split_string(rtrim(readline()));
    int n = atoi(inp[0]);
    int k = atoi(inp[1]);
    int l = atoi(inp[2]);

    //printf("%d %d %d\n", n, k, l);

    char *s = rtrim(readline());
    //printf("s = %s\n", s);
    //printf("len s = %d\n", strlen(s));

    char *s_upper = (char *)malloc(sizeof(char) * strlen(s));
    char *s_lower = (char *)malloc(sizeof(char) * strlen(s));
    for (int i = 0; i < n; i++)
    {
        char c = s[i];
        if (c >= 'A' && c <= 'Z')
        { // c is uppercase
            s_upper[i] = '1';
            s_lower[i] = '0';
        }
        else
        {
            s_upper[i] = '0';
            s_lower[i] = '1';
        }
    }
    //printf("s_upper = %s \n", s_upper);

    int *dp_table = (int *)malloc(n * sizeof(int));
    int *cnt_table = (int *)malloc(n * sizeof(int));

    int theta = binary_search(n, k, l, s_upper, dp_table, cnt_table);
    compute_dp(n, dp_table, cnt_table, l, s_upper, theta);
    int ans1 = n - (dp_table[n - 1] + theta * k);

    theta = binary_search(n, k, l, s_lower, dp_table, cnt_table);
    compute_dp(n, dp_table, cnt_table, l, s_lower, theta);
    int ans2 = n - (dp_table[n - 1] + theta * k);

    int ans = min(ans1, ans2);
    printf("%d\n", ans);
}

main();

char *readline()
{
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char *data = malloc(alloc_length);

    while (true)
    {
        char *cursor = data + data_length;
        char *line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line)
        {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n')
        {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data)
        {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n')
    {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data)
        {
            data = '\0';
        }
    }
    else
    {
        data = realloc(data, data_length + 1);

        if (!data)
        {
            data = '\0';
        }
        else
        {
            data[data_length] = '\0';
        }
    }

    return data;
}

char *ltrim(char *str)
{
    if (!str)
    {
        return '\0';
    }

    if (!*str)
    {
        return str;
    }

    while (*str != '\0' && isspace(*str))
    {
        str++;
    }

    return str;
}

char *rtrim(char *str)
{
    if (!str)
    {
        return '\0';
    }

    if (!*str)
    {
        return str;
    }

    char *end = str + strlen(str) - 1;

    while (end >= str && isspace(*end))
    {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

char **split_string(char *str)
{
    char **splits = NULL;
    char *token = strtok(str, " ");

    int spaces = 0;

    while (token)
    {
        splits = realloc(splits, sizeof(char *) * ++spaces);

        if (!splits)
        {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}

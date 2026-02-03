class Solution {
  private:
    void dfs(int node,vector<int>ls[],int vis[]){
        vis[node]=1;
        for(auto it:ls[node]){
            if(!vis[it]){
                dfs(it,ls,vis);
            }
        }
    }
  public:
    int numProvinces(vector<vector<int>> adj, int V) {
        // code here
        vector<int>ls[V];
        for(int i=0;i<V;i++){
            for(int j=0;j<V;j++){
                if(adj[i][j]==1 && i!=j){
                    ls[i].push_back(j);
                    ls[j].push_back(i);
                }
            }
        }
        
        int vis[V]={0};
        int cnt=0;
        for(int i=0;i<V;i++){
            if(!vis[i]){
                cnt++;
                dfs(i,ls,vis);
            }
        }
        
        return cnt;
        
    }
};
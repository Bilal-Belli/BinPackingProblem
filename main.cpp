#include <iostream>
#include <stack>
#include <vector>
#include <numeric>
#include <algorithm>
#include <fstream>
#include <ctime>
#define N 150

std::vector<int> items_weights;

typedef struct ActiveNode {
    std::vector<int> bins;//nombre de packets utilisé jusqu'à maintenant pour effectuer une estimation 
    std::vector<int> remaining_items;//les objets restants à remettre (sont identifié avec leurs )
    std::vector<int> items;// contient le numéro du packet affecté au client
    int index;//contient l'index de l'objet à placer
}ActiveNode;

int estim(ActiveNode node){
    int total_weight= 0;
    if(node.remaining_items.size()!= 0)
        total_weight = std::accumulate(node.remaining_items.begin(), node.remaining_items.end(), 0);
    int x = 0;
    std::vector<int> estim;
    if(node.bins.size()>0){
        int total_wasted_space = N*node.bins.size() - total_weight;
        

        
        x = total_wasted_space/N + (total_wasted_space%N!=0);
        for(auto& bin:node.bins)
            if(node.remaining_items[0]<(N-bin))
            {
                x--;
                break;
            }

    }   
    //std::cout<<"\n\n"<<"the estimation of the node is  : " << node.bins.size()+ total_weight/N + (total_weight%N!=0) -  x<<"\n\n";
    /* */
    
    return  node.bins.size()+ total_weight/N + (total_weight%N!=0)/*-x*/;
}

ActiveNode fit(ActiveNode node){
    ActiveNode ret_node;
    //copy the bins
    ret_node.bins = node.bins;
    //since we are going to insert an additional element the remaining items left are decreased
    ret_node.remaining_items.reserve(node.items.size() - 1);
    //
    ret_node.items = node.items;
    //we are going to begin since the begining
    ret_node.index = 0;
    //process of insertion of insertion from node to retnode
    bool inserted = false;
    for (int i = 0; i < node.bins.size(); i++) {
        if (node.remaining_items[node.index] <= N - node.bins[i] ) {
            //add to the bin 
            ret_node.bins[i] += node.remaining_items[node.index];
            //put the bin number on the item in items
            
            for(int j = 0;j<node.items.size();j++){
                if(items_weights[j] == node.remaining_items[node.index] && node.items[j]==-1){
                    ret_node.items[j]= i;
                    break;
                }
            }
            
            inserted = true;
            break;
        }
    }
    if (!inserted) {
        ret_node.bins.push_back(node.remaining_items[node.index]);
        for(int j = 0;j<node.items.size();j++){
            if(items_weights[j] == node.remaining_items[node.index] && node.items[j]==-1){
                ret_node.items[j]= ret_node.bins.size()-1;
                break;
            }
        }
        
        
        
    }

    //copying the items from node to ret
        
    for (int i = 0; i < node.remaining_items.size(); i++) {
        if (i != node.index) {
            ret_node.remaining_items.push_back(node.remaining_items[i]);
        }
    }
    
    return ret_node;

}

void print_active_node(ActiveNode node){
    std::cout<<"Node" <<"\n";
    std::cout << "Bins list :"<<"\n";
    int bin_it = 0;
    for (auto& sp_occ:node.bins){
        std::cout<<"space occupied in bin :"<<bin_it<< " : " << sp_occ<<"\n"; 
        bin_it ++;
    }

    std::cout << "Items list :"<<"\n";
    int item_it=0;
    for (auto& item:node.items){
        std::cout<<"bin of the item :"<<item_it<< " : " << item<<"\n"; 
        item_it++;

    }

    std::cout << "Remaining Items :" <<"\n";
    int rem_it =0;
    for (auto& rem_item:node.remaining_items){
        std::cout<<"item weights :" <<rem_it<< " : "<< rem_item <<"\n"; 
        rem_it++;
    }

    std::cout << "index" <<node.index<<"\n";
    

}


int main() {
    std::stack<ActiveNode> stack_trace;
    std::vector<int>items_bin_number;
    std::vector<int> trivial_solution;
    
    //reading weights
    std::ifstream infile("BPP_50_150_0.1_0.8_8.txt");
    int weight;  
    int i=0;  
    while (infile >> weight) {    // read each integer from the file
        items_weights.push_back(weight);    // push the integer into the vector
        items_bin_number.push_back(-1);
        trivial_solution.push_back(i);
        i++;
    }
    infile.close();

    int optimal_solution = items_weights.size();
    ActiveNode optimal_node = {items_weights,{},trivial_solution,0};
    ActiveNode node ={{},items_weights,items_bin_number,0} ;
    int pruning = 0;
    stack_trace.push(node);
    int preced=-1;
    int current;

std::clock_t start_time = std::clock(); // Get the starting time
    // Code to measure time for goes here
    

    while (stack_trace.size()!=0 )
    {
        std::cout <<"ACTUAL OPTIMAL SOLUTION "<<optimal_solution<<"\n\n";
        //get the active node

        node = stack_trace.top();
        stack_trace.pop();
        //print_active_node(node);
        
        //check if it is a leafnode
        if(node.remaining_items.size()==0){
            if(node.bins.size()<optimal_solution){
                optimal_solution = node.bins.size();
                optimal_node = node;
            }
        }//else 
        else{
            
            //check if it is worth to continue 
                std::cout <<"Estimation is :"<<estim(node)<<"\n\n";
                if(estim(node) < optimal_solution && !(node.index!=0 && node.remaining_items[node.index-1]==node.remaining_items[node.index])){
                    //check if it is not the last node to insert it is like a time to live for a node
                    if (node.index!=node.remaining_items.size()-1)
                        stack_trace.push({node.bins, node.remaining_items, node.items, node.index+1});
                    
                    node = fit(node);
                
                    stack_trace.push(node);
                    

                }
                else{
                    pruning++;
                }
               
        }
    

    }
    
std::clock_t end_time = std::clock(); // Get the ending time
    double elapsed_time = (double)(end_time - start_time) / CLOCKS_PER_SEC; // 

    //printing the results
    
    for(int i = 0 ; i < optimal_node.bins.size() ;i++){
        std::cout << "bin : "<<i<<"\n";
        for(int j = 0;j < optimal_node.items.size(); j ++){
            if(optimal_node.items[j]==i){
                std::cout << items_weights[j] <<",";
            }
            
        }
        std::cout<<"\n";
    }

    std::cout<<elapsed_time<<"\n\n";
    return 0;
    
}
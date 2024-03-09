#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <unistd.h>

#define HOSTNAME "vortex.labs.overthewire.org"
#define PORT 5842
#define LEN 255

#define SA struct sockaddr

void request(int sockfd)
{
	char res[LEN];
	bzero(res, sizeof(res));
	read(sockfd, res, sizeof(res));
	printf("%s", res);

	struct bytes {
		unsigned int a, b, c, d;
	} *x = (struct bytes *) &res;
	unsigned int y = x->a + x->b + x->c + x->d;
	write(sockfd, &y, 4);

	bzero(res, sizeof(res));
	read(sockfd, res, sizeof(res));
	printf("%s", res);
}

int resolveHost(char *hostname, char *ip);

int main()
{
	char host[16];
	int sockfd, connfd;
	struct sockaddr_in servaddr, cli;
	sockfd = socket(AF_INET, SOCK_STREAM, 0);

	if (sockfd == -1)
	{
		printf("Socket creation failed...\n");
		exit(0);
	}

	resolveHost(HOSTNAME, host);
	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = inet_addr(host);
	servaddr.sin_port = htons(PORT);

	if (connect(sockfd, (SA *)&servaddr, sizeof(servaddr)) != 0)
	{
		printf("Connection with the server failed...\n");
		exit(0);
	}
	request(sockfd);
	close(sockfd);
}

int resolveHost(char *hostname, char *ip)
{
	struct hostent *hent;
	struct in_addr **addr_list;
	int i;
	if ((hent = gethostbyname(hostname)) == NULL)
	{
		herror("gethostbyname error");
		return 1;
	}
	addr_list = (struct in_addr **)hent->h_addr_list;
	for (i = 0; addr_list[i] != NULL; i++)
	{
		strcpy(ip, inet_ntoa(*addr_list[i]));
		return 0;
	}
	return 1;
}
import { routeTable as authRouteTable } from 'src/auth/routeTable';
import { RouteTable } from 'src/utils/RouteTable';

export const routeTable = new RouteTable();
routeTable.addTable(authRouteTable, '');

export const routes = routeTable.routeByName;
